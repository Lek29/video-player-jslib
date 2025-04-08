from livereload import Server

server = Server()

server.watch('index.html')
server.watch('css/style.css')

server.serve(root='.')