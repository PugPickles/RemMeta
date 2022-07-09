import os
from PIL import Image
from PIL.ExifTags import TAGS


pathIn = os.path.abspath("in")
pathOut = os.path.abspath("out")


def main():
    try:
        files = os.listdir(pathIn)

        if len(files) == 0:
            print("\n\nNo files found!\n")
            return


        def metaData(metaData):
            try:
                print("\n>>> METADATA:\n")
                for tag_id in metaData:
                    tag = TAGS.get(tag_id, tag_id)
                    content = metaData.get(tag_id)

                    if isinstance(content, bytes):
                        content = content.decode()

                    print(f'{tag:25}: {content}')
                print()

            except Exception as e:
                print("\n\n>>> ERROR: " + str(e))
                return


        for img in files:
            print("\n\n- - - - - - - - - - - - - - - - - - - - - -")
            print("\n>>> Found: " + img)

            image = Image.open(pathIn + "/" + img)
            metaData(image.getexif())

            data = list(image.getdata())
            clearImg = Image.new(image.mode, image.size)
            clearImg.putdata(data)
            print("\n\n\n>>> MetaData rem.: " + img + "\n")

            clearImg.save(pathOut + "/" + img)
            print(">>> Saved: " + img + "\n")

            clearImageDat = Image.open(pathOut + "/" + img)
            metaData(clearImageDat.getexif())
            clearImageDat.close()


    except Exception as e:
        print(e)
        return


    finally:
        input("\n\nPress enter to exit")



if __name__ == "__main__":
    main()
