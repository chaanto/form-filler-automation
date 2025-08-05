from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta
from selenium.webdriver.chrome.options import Options
import time


# テキストエリア型　自動入力を用意する
def input_text_autocomplete(driver, field_id, value_input):
    input_el = WebDriverWait(driver, 2).until(
        EC.element_to_be_clickable((By.ID, field_id))
    )
    input_el.clear()
    input_el.send_keys(value_input)


# プルダウン型　自動入力を用意する
def option_dropdown(driver, select_id, dropdown_value):
    select_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, select_id))
    )
    dropdown = Select(select_element)
    dropdown.select_by_value(dropdown_value)


def wait_and_select_dropdown(driver, dropdown_id, value_target, timeout=10):
    def dropdown_has_options(driver):
        try:
            dropdown = driver.find_element(By.ID, dropdown_id)
            options = dropdown.find_elements(By.TAG_NAME, "option")
            return len(options) > 1
        except NoSuchElementException:
            return NoSuchElementException(driver)

    WebDriverWait(driver, timeout).until(dropdown_has_options)

    dropdown = driver.find_element(By.ID, dropdown_id)
    Select(dropdown).select_by_value(value_target)


# ラジオボタン型　自動入力を用意する
def radio_button_selected(driver, radioBtn_Id, target_value):
    radios = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.ID, radioBtn_Id))
    )

    for radio in radios:
        if radio.get_attribute("value") == target_value:
            if not radio.is_selected():
                radio.click()
            return


def radio_button_selected_kubun(driver, radioBtn_Id, target_value):
    radios = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.NAME, radioBtn_Id))
    )

    for radio in radios:
        if radio.get_attribute("value") == target_value:
            if not radio.is_selected():
                radio.click()
            return


# ボタン　自動操作を用意する
def button_click_by_value(driver):
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@data-button-kind='write' and text()='登録']"))
    )
    button.click()


def button_click_by_data_name(driver, data_name_id):
    xpath = f"//button[@data-name-id='{data_name_id}']"
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, xpath))
    )
    button.click()


def button_click_by_id(driver, element_id):
    tombol = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, element_id))
    )
    tombol.click()


# 時刻　自動操作を用意する
def input_time(driver, time_id, time_value, timeout=10):
    time_input = WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable((By.ID, time_id))
    )
    time_input.clear()
    time_input.send_keys(time_value)


# ログイン画面
def login_action(driver):
    input_text_autocomplete(driver, "staff", "admin")  # 自動入力
    button_click_by_value(driver, "ログイン")  # 自動ログイン


# 自動入力の値をセットし、各フィールドに表示する                             
def runProgram(driver):
    """ 人定項目 """
    option_dropdown(driver, "ryuchiKbn", "2")  # 留置区分
    input_text_autocomplete(driver, "kanaName", "ﾔﾏﾀﾞｲﾁﾛｳ")  # カナ氏名
    input_text_autocomplete(driver, "kanjiName", "山田一郎")  # 漢字氏名
    radio_button_selected(driver, "sexCd1", "1")  # 性別  

    # 生年月日不詳
    driver.execute_script('document.getElementById("birthdateFushouFlg1").checked = true;')

    # modal 出生地選択
    button_click_by_data_name(driver, "seichi")  # 出生地選択
    wait_and_select_dropdown(driver, "schSeichiKen", "30")
    wait_and_select_dropdown(driver, "schSeichiShikutyouson", "30101")
    time.sleep(1)
    button_click_by_id(driver, "seichiSelect")

    # modal 本籍検索
    button_click_by_data_name(driver, "honseki")  # 本籍検索  
    wait_and_select_dropdown(driver, "schKen", "10")
    wait_and_select_dropdown(driver, "schShikutyouson", "10100")
    time.sleep(1)
    button_click_by_id(driver, "jushoSelect")

    # modal 住所検索
    button_click_by_data_name(driver, "address")  # 住所検索
    wait_and_select_dropdown(driver, "schKen", "30")
    wait_and_select_dropdown(driver, "schShikutyouson", "30100")
    time.sleep(1)
    button_click_by_id(driver, "jushoSelect")

    # modal 国籍検索
    button_click_by_data_name(driver, "kokuseki")  # 国籍検索
    wait_and_select_dropdown(driver, "schKokusekiKen", "100")
    wait_and_select_dropdown(driver, "schKokusekiShikutyouson", "00101")
    time.sleep(1)
    button_click_by_id(driver, "kokusekiSelect")

    # modal 職業検索
    button_click_by_data_name(driver, "job")  # 職業検索
    wait_and_select_dropdown(driver, "schDaiBunrui", "000")
    wait_and_select_dropdown(driver, "schChuBunrui", "010")
    wait_and_select_dropdown(driver, "schShokugyou", "011")
    time.sleep(1)
    button_click_by_id(driver, "shokugyouSelect")

    option_dropdown(driver, "soshikiCd", "2")

    """ 新入項目 """
    option_dropdown(driver, "szkFacCd", "100,11")  # 処遇所属
    input_text_autocomplete(driver, "shoguBikou", "処遇所属")  # 処遇備考
    input_text_autocomplete(driver, "ryuchiNo", "111")  # 留置番号
    option_dropdown(driver, "ryuchiRiyuCd", "01")  # 留置理由コード
    input_text_autocomplete(driver, "kyoshitsuNo", "222")  # 居室番号
    option_dropdown(driver, "kioushouFlg", "2")  # 既往症有無

    input_text_autocomplete(driver, "height", "170")  # 身長   
    input_text_autocomplete(driver, "weight", "70")  # 体重
    input_text_autocomplete(driver, "footSize", "42")  # 足のサイズ
    option_dropdown(driver, "taikakuCd", "2")  # 体格コード
    option_dropdown(driver, "meganeCd", "02")  # 眼鏡コード
    option_dropdown(driver, "bloodTypeCd", "4")  # 血液型コード
    option_dropdown(driver, "kikiudeCd", "2")  # 聴覚障害コード
    option_dropdown(driver, "kamigataCd", "02")  # 髪型コード
    option_dropdown(driver, "irezumiFlg", "2")  # 入れ墨有無
    option_dropdown(driver, "kamiiroCd", "1")  # 髪色コード
    option_dropdown(driver, "kaogataCd", "1")  # 顔型コード
    option_dropdown(driver, "ninshinFlg", "1")  # 妊娠
    option_dropdown(driver, "languageCd", "001")  # 会話言語

    """事件項目"""
    # modal 罪名検索
    button_click_by_data_name(driver, "taihoZaimei1")  # 逮捕罪名検索
    wait_and_select_dropdown(driver, "schShubetsu", "1")  # 罪名種別
    wait_and_select_dropdown(driver, "schZaimei", "09200")  # 罪名
    time.sleep(1)
    button_click_by_id(driver, "zaimeiSelect")  # 罪名選択ボタン 

    input_text_autocomplete(driver, "taihoAge", "12")
    radio_button_selected(driver, "shounenFlg1", "0")

    # modal 所属検索
    button_click_by_data_name(driver, "taihoSzk")  # 所属検索
    radio_button_selected_kubun(driver, "kubun", "1")
    wait_and_select_dropdown(driver, "schZenkokuHoumen", "7071")
    wait_and_select_dropdown(driver, "schZenkokuSyozoku", "30100")
    time.sleep(1)
    button_click_by_id(driver, "syozokuZenkokuSelect")

    time.sleep(2)
    option_dropdown(driver, "kakariList", "100600")  # 捜査係
    option_dropdown(driver, "taihoshaKanshokuCd", "01")  # 捜査幹部官職

    input_text_autocomplete(driver, "taihoshaName", "逮捕者氏名")  # 逮捕者氏名
    option_dropdown(driver, "taihoKindCd", "01")

    # 逮捕日時
    today_dt = datetime.today()
    today = today_dt.strftime('%Y/%m/%d')
    tomorrow = (today_dt + timedelta(days=1)).strftime('%Y/%m/%d')
    driver.execute_script('document.getElementById("taihoDate").value = arguments[0];', today)
    input_time(driver, "taihoTime", "14:30")

    # 事件開始日時
    driver.execute_script('document.getElementById("jikenStartDate").value = arguments[0];', tomorrow)
    input_time(driver, "jikenStartTime", "15:30")

    option_dropdown(driver, "ryuchijiMigaraCd", "2")  # 留置事由身柄コード    

    # modal 日付選択
    button_click_by_data_name(driver, "szk")  # 逮捕日付選択
    radio_button_selected_kubun(driver, "kubun", "1")
    wait_and_select_dropdown(driver, "schZenkokuHoumen", "7072")
    wait_and_select_dropdown(driver, "schZenkokuSyozoku", "30215")
    time.sleep(1)
    button_click_by_id(driver, "syozokuZenkokuSelect")

    wait_and_select_dropdown(driver, "kakariListSousa", "215600")  # 捜査係
    option_dropdown(driver, "kanshokuCd", "01")  # 捜査幹部官職
    input_text_autocomplete(driver, "kanbuName", "捜査幹部氏名")  # 捜査幹部氏名

    option_dropdown(driver, "kakariListSousaSyunin", "215600")  # 捜査係主任
    option_dropdown(driver, "shuninKanshokuCd", "01")  # 捜査主任官職

    input_text_autocomplete(driver, "shuninName", "捜査主任官氏名")  # 捜査主任官氏名


# メインプログラム
def main():
    options = Options()
    # options.add_argument("--headless")         # GUI表示なし
    # options.add_argument("--disable-gpu")      # GPU無効化（Windows環境用）
    options.add_argument("--window-size=1920,1080")  # 画面サイズ指定（任意）
    options.add_argument("--force-device-scale-factor=0.7")  # 70%に設定

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    # URLセット
    driver.get('http://localhost:8080/ryuchisys/login_dummy/')

    # 麹町署をクリック（data-name-id="kojimachi" と仮定）
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@formaction='/ryuchisys/login/100003/pc-100-11']"))
    )
    button.click()

    # 少し時間を取ってメニュー展開を待つ
    time.sleep(2)  # JS描画完了待ち

    # メガメニュー「入力業務」を開く
    menu_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), '入力業務')]"))
    )
    menu_button.click()

    # 少し時間を取ってメニュー展開を待つ
    time.sleep(2)  # JS描画完了待ち

    # 少し待ってからリンクを探す
    link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "higishaLink"))
    )
    link.click()

    # 自動入力対象となる画面をセットする
    target_url = "http://localhost:8080/ryuchisys/viewHigishaEdit"

    # ログアウト後、改めて自動ログイン
    login_url = "http://localhost:8080/ryuchisys/login_dummy/"
    end_url = ""

    try:
        while True:
            current_url = driver.current_url.split(";")[0]

            if current_url == target_url and current_url != end_url:
                runProgram(driver)
                end_url = current_url
                time.sleep(1)
                button_click_by_value(driver)

            else:
                print(f"Waiting... Now URL is: {current_url}", end="\r")
                if current_url != target_url:
                    end_url = ""

            time.sleep(1)

    except KeyboardInterrupt:
        input("click ENTER to close program")
        driver.quit()


main()
