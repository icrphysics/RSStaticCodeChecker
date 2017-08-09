server_adress = "http://localhost:{}/"

def get_port():
	return 1846

def get_server():
    return server_adress.format(get_port())

def get_version():
    return "R6"