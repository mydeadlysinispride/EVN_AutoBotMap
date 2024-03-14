import pyautogui
import time
import os
import pandas as pd

# image_path
search_btn_img_path = r".\images\search_btn.png"
upload_img_btn_path = r".\images\upload_img.png"

def read_data(file_path):
    df = pd.read_excel(file_path)
    df_grouped = df.groupby('Folder name').agg({'Coordinate': 'first', 'Direct Link': list}).reset_index()
    return df_grouped

def find_image_on_screen(image_path, confidence=0.8):
    if os.path.exists(image_path):
        # Find the position of the image
        image_position = pyautogui.locateOnScreen(image_path, confidence=confidence)
        time.sleep(2)
        return image_position
    else:
        print(f"Image not found at path: {image_path}")
        return None
    
def get_center_position(box):
    if box is not None:
        center_x = box.left + box.width / 2
        center_y = box.top + box.height / 2
        return (center_x, center_y)
    else:
        print("Image not found on the screen.")
        return None
    
def main():
    time.sleep(10)
    df_grouped = read_data('location.xlsx')
    for filename in df_grouped['Folder name']:
        print("...Start to upload image to Cot :", filename)
        search_btn = find_image_on_screen(search_btn_img_path)
        search_btn_center = get_center_position(search_btn)
        # move the mouse to search button and click
        pyautogui.moveTo(search_btn_center)
        pyautogui.click()
        time.sleep(1)

        # press tab to move to the next coordinate
        pyautogui.press('tab')
        num_direct_links = len(df_grouped[df_grouped['Folder name'] == filename]['Direct Link'].iloc[0])
        print("So direct link cua folder: ", num_direct_links)

        # lay ra direct link
        direct_link = df_grouped[df_grouped['Folder name'] == filename]['Direct Link'].iloc[0]

        i = 0
        # Vong lap de upload anh cua 1 Cot
        while True:
            if num_direct_links == 0:
                break
            # find the upload button and click
            upload_btn = find_image_on_screen(upload_img_btn_path, confidence=0.7)
            upload_btn_center = get_center_position(upload_btn)
            pyautogui.moveTo(upload_btn_center)
            pyautogui.click()
            time.sleep(3)

            # choose upload by enter link 
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('right')
            pyautogui.press('right')
            time.sleep(1) 
            pyautogui.press('enter')
            pyautogui.press('tab')
            time.sleep(1)

            # type the direct link and press enter to upload
            pyautogui.write(direct_link[i])
            time.sleep(10)
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('enter')
            time.sleep(3)
            i+=1
            num_direct_links-=1

            # press enter to confirm the upload
            pyautogui.press('enter')
            pyautogui.press('enter')
            pyautogui.press('enter')
            time.sleep(3)

if __name__ == "__main__":
    main()



        




