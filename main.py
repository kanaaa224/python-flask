def main():
    from api import create

    api = create()
    api.run(host='0.0.0.0', port=5000, debug=True)

if __name__ == '__main__':
    main()