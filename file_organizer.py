import os
import shutil


CATEGORIES = {
    "Images": {".jpg", ".jpeg", ".png", ".gif", ".webp"},
    "Documents": {".pdf", ".doc", ".docx", ".txt"},
    "Audio": {".mp3", ".wav", ".flac"},
    "Videos": {".mp4", ".mov", ".avi"},
}


def organize_folder(folder):
    for filename in os.listdir(folder):
        source = os.path.join(folder, filename)

        if not os.path.isfile(source):
            continue

        extension = os.path.splitext(filename)[1].lower()
        category = "Other"

        for name, extensions in CATEGORIES.items():
            if extension in extensions:
                category = name
                break

        destination_folder = os.path.join(folder, category)
        os.makedirs(destination_folder, exist_ok=True)

        shutil.move(source, os.path.join(destination_folder, filename))


if __name__ == "__main__":
    folder = input("Enter folder path: ").strip()
    organize_folder(folder)
    print("Files organized successfully.")
