'use strict';
// The module 'vscode' contains the VS Code extensibility API
// Import the module and reference it with the alias vscode in your code below
import * as vscode from 'vscode';
// this method is called when your extension is activated
// your extension is activated the very first time the command is executed
export function activate(context: vscode.ExtensionContext) {

    // Use the console to output diagnostic information (console.log) and errors (console.error)
    // This line of code will only be executed once when your extension is activated
    console.log('Congratulations, your extension "rsstaticcodechecker-vscode-ext" is now active!');

    // The command has been defined in the package.json file
    // Now provide the implementation of the command with  registerCommand
    // The commandId parameter must match the command field in package.json
    let disposable_1 = vscode.commands.registerCommand('extension.runRSSCCOnFile', () => {
        return runOnFile();
    });

    let disposable_2 = vscode.commands.registerCommand('extension.runRSSCCOnFolder', () => {
        return runOnFolder();
    });

    context.subscriptions.push(disposable_1);
    context.subscriptions.push(disposable_2);


    let previewUri = vscode.Uri.parse('resultview://authority/resultview');
    let fs = require('fs');
    let path = require('path');
    var child_process = require('child_process');
    let htmlOutput = path.join(__dirname, '../..', 'tmp', 'out.html');

	class TextDocumentContentProvider implements vscode.TextDocumentContentProvider {
		private _onDidChange = new vscode.EventEmitter<vscode.Uri>();

        private loading :boolean = false;

		public provideTextDocumentContent(uri: vscode.Uri): string {
			return this.getHtml();
		}

		get onDidChange(): vscode.Event<vscode.Uri> {
			return this._onDidChange.event;
		}

		public update(uri: vscode.Uri) {
			this._onDidChange.fire(uri);
        }

        private getHtml() :string
        {
            let fs = require('fs');
            let path = require('path');
            let htmlString = "";
            if(this.loading)
            {
                let htmlPathLoading = path.join(__dirname, '../..', 'html', 'loading.html');
                htmlString = fs.readFileSync(htmlPathLoading, 'utf8');
            }else
            {
                htmlString = fs.readFileSync(htmlOutput, "utf8");
            }
            return htmlString
        }

        public setLoading(loadingState :boolean)
        {
            this.loading = loadingState;
        }
    }

    let oldJob = undefined;

    let provider = new TextDocumentContentProvider();
    let registration = vscode.workspace.registerTextDocumentContentProvider('resultview', provider);

    function runOnFile()
    {
        if(!vscode.window.activeTextEditor)
        {
            vscode.window.showErrorMessage("No file opened to analyze");
            return;
        }
        let file = vscode.window.activeTextEditor.document.fileName;
        startLoading();
        executeWithArguments(["--file", file]);
        return openResultView();
    }

    function runOnFolder()
    {
        let folder = vscode.workspace.rootPath;
        startLoading();
        executeWithArguments(["--folder", folder]);
        return openResultView();
    }

    function executeWithArguments(args : Array<string>)
    {
        if(oldJob)
        {
            console.log("KILLING OLD JOB!!!");
            oldJob.kill("SIGINT"); //doesnt yet work...
        }
        args.push("--output");
        args.push(htmlOutput.toString());
        args.push("--html");
        args.push("True");

        let executingFile = "rs_code_scanner";
        console.log(executingFile);
        if (!/^win/.test(process.platform)) {
            var ls = child_process.spawn(executingFile, args);
        }else
        {
            args.unshift(executingFile)
            args.unshift("/c");
            args.unshift("/s");
            var ls = child_process.spawn("cmd", args);
            console.log(args);
        }
        ls.stdout.on('data', (raw_data) => {
            console.log('stdout: ' + "  " + raw_data);
        });

        ls.stderr.on('data', (data)  => {
            console.log('stderr: ' + data);
            vscode.window.showErrorMessage(data);
        });

        ls.on('exit', (code)  => {
            console.log('child process exited with code ' + code);
            if(code == null)
            {
                return; //Task was manually stopped
            }
            loadingFinished();
        });

        oldJob = ls;
    }

    function startLoading()
    {
        provider.setLoading(true);
        provider.update(previewUri);
    }

    function loadingFinished()
    {
        provider.setLoading(false);
        provider.update(previewUri);
    }


    function openResultView()
    {
        return vscode.commands.executeCommand('vscode.previewHtml', previewUri, vscode.ViewColumn.Two, 'Static Code Scanner Result').then((success) => {
        }, (reason) => {
            vscode.window.showErrorMessage(reason);
        });
    }

}

// this method is called when your extension is deactivated
export function deactivate() {
}

