import aria2p

# initialization, these are the default values
aria2 = aria2p.API(
    aria2p.Client(
        host="http://192.168.1.222",
        port=6800,
        secret="222"
    )
)
# # list downloads
# downloads = aria2.get_downloads()
# print(downloads)