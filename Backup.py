import dirsync
import os

src = "Your source"
dest = "Your destination"

if os.path.exists(dest):
    dirsync.sync(src, dest, 'sync', purge=True)
else:
    print("Erreur fatale, le disque Réseau n'est pas monté")
