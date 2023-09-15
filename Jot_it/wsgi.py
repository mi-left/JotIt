import jot_it_server

if __name__ == '__main__':
    jot_it_server.main()
    jot_it_server.app.run(host='0.0.0.0', port=80)