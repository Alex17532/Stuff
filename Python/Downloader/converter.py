import zipfile
         
path = input("Full path: ")[:-4]+".zip"
jungle_zip = zipfile.ZipFile(path, 'w')
jungle_zip.write(path+"", compress_type=zipfile.ZIP_DEFLATED)
 
jungle_zip.close()