import random
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import urljoin

def scrape_data(url):
    #変数定義
    head_url = "https://club.battlespirits.com"
    images = []
    card_name = []
    card_counts =[]
    counts =[]
    deck =[]
    n = 0  # 契約スピリット判定用
    
    # 契約スピリットリスト
    keis = [
        "相棒竜グロウ", 
        "相棒狼ランポ",
        "相棒騎士バット",
        "相棒機スターク",
        "相棒鳥フェニル",
        "相棒鮫シャック",
        "相棒虫ガタル",
        "月光龍ストライク・ジークヴルム",
        "相棒翼竜テラード",
        "相棒獅子ラオン",
        "悪魔バイス",
        "νガンダム",
        "Ξガンダム",
        "ガンダム・エアリアル",
        "イアン",
        "ショコラ",
        "ムゲン",
        "相棒魔卿ジャバド",
        "放浪者ダンのブレイドラ",
        "相棒無頼ヴリック",
        "相棒猫フェルマ",
        "[ずっと一緒に]フォンニーナ",
        "[ずっと一緒に]リアス・ウロヴォルン",
        "鏑木・T・虎徹＆バーナビー・ブルックス Jr.",
        "カリーナ・ライル＆ライアン・ゴールドスミス",
        "ネイサン・シーモア＆キース・グッドマン",
        "イワン・カレリン＆アントニオ・ロペス",
        "仙石 昴＆トーマス・トーラス",
        "ホァン・パオリン＆ラーラ・チャイコスカヤ",
        "テッペンバディ アイボウ"
    ]
    
    # HTMLを解析
    html = urlopen(url)
    data = html.read()
    html = data.decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    
    # 解析したHTMLから任意の部分のみを抽出
    images = soup.select("main > section > div > ul > li")
    card_name = soup.select("main > section > div > ul > li")
    
    for i in range(len(images)):
        images[i] = images[i].find("img")
        card_name[i] = card_name[i].find("img")
        if images[i].get("src").endswith(".jpg"): # imgタグ内の.jpgであるsrcタグを取得
            images[i] = images[i].get("src")
        if card_name[i].get("alt"):
            card_name[i] = card_name[i].get("alt")
    
    card_counts = soup.find_all('p', class_='cardCount')
    for i in range(len(card_counts)):
        if card_counts[i].string == "1枚":
            counts.append(1)
        elif card_counts[i].string == "2枚":
            counts.append(2)
        else:
            counts.append(3)
    
    #契約スピリットがいる場合
    for i in range(len(images)):
        for j in range(len(keis)):
            if card_name[i] == keis[j]:
                keiyaku = images[i]
                counts[i] = counts[i] - 1
                n =1
                break
    # デッキ作成
    for i in range(len(counts)):
        for j in range(counts[i]):
            deck.append(head_url + images[i])
    # シャッフル
    shuffle_deck = deck
    random.shuffle(shuffle_deck)
    if n == 1:
        deck.insert(0, head_url + keiyaku)
    
    return shuffle_deck
    
        
    
    