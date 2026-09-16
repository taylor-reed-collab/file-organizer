import os
import tempfile
import unittest

from file_organizer import organize_folder


class TestFileOrganizer(unittest.TestCase):
    def test_organize_files(self):
        with tempfile.TemporaryDirectory() as folder:
            open(os.path.join(folder, "photo.jpg"), "w").close()
            open(os.path.join(folder, "report.pdf"), "w").close()
            open(os.path.join(folder, "song.mp3"), "w").close()
            open(os.path.join(folder, "movie.mp4"), "w").close()

            organize_folder(folder)

            self.assertTrue(os.path.exists(
                os.path.join(folder, "Images", "photo.jpg")
            ))
            self.assertTrue(os.path.exists(
                os.path.join(folder, "Documents", "report.pdf")
            ))
            self.assertTrue(os.path.exists(
                os.path.join(folder, "Audio", "song.mp3")
            ))
            self.assertTrue(os.path.exists(
                os.path.join(folder, "Videos", "movie.mp4")
            ))


if __name__ == "__main__":
    unittest.main()
