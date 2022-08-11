import dirsync
import os

src = "W:\TEMP"
dest = "Z:\Data\Archive\ArchiveTemp"

if os.path.exists(dest):
    dirsync.sync(src, dest, 'sync', purge=True)
else:
    print("Erreur fatale, le disque Réseau n'est pas monté")