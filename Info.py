from kivymd.app import MDApp
from kivymd.uix.screen import *
from kivymd.uix.textfield import *
from kivymd.uix.button import *
from kivymd.uix.dialog import *
from kivy.lang import *
from kivymd.uix.menu import MDDropdownMenu
import requests,webbrowser
import requests,sys,time,os,random
import mechanize,requests,time
from telebot import types
from bs4 import BeautifulSoup
from flask import *
class Hamody(MDApp):
	def build(self):
		self.screen = MDScreen()
		self.id = MDTextField(
		mode = "rectangle",
		hint_text = "ID",
		helper_text = "ENTER ID  TELEGRAM",
		helper_text_mode = "on_focus",
		pos_hint = {"center_x": 0.5 ,"center_y" : 0.6},
		size_hint_x = 0.8,
		icon_right = "telegram",
		multiline=False,
		allow_copy = True,
		width = 340,
		required = True)
		self.token = MDTextField(
		mode = "rectangle",
		hint_text = "TOKEN",
		helper_text = "ENTER TOKEN TELEGRAM",
		helper_text_mode = "on_focus",
		pos_hint = {"center_x": 0.5 ,"center_y" : 0.5},
		size_hint_x = 0.8,
		icon_right = "telegram",
		multiline=False,
		allow_copy = True,
		width = 340,
		required = True)
		self.user = MDTextField(
		mode = "rectangle",
		hint_text = "USER",
		helper_text = "ENTER USER INSTGRAM",
		helper_text_mode = "on_focus",
		pos_hint = {"center_x": 0.5 ,"center_y" : 0.7},
		size_hint_x = 0.8,
		icon_right = "instgram",
		multiline=False,
		allow_copy = True,
		width = 340,
		required = True
		)
		self.theme_cls.theme_style = "Dark"
		self.theme_cls.primary_palette = "Orange"
		self.menu = MDDropdownMenu(
    ver_growth="up",
)
		insta = MDFloatingActionButton(
		icon = "instagram",
		pos_hint = {"center_x":0.1 , "center_y":0.3},
		on_release = self.instagram
		)
		an = MDFloatingActionButton(
		icon = "android",
		pos_hint = {"center_x":0.5, "center_y":0.8},
		)
		python = MDFloatingActionButton(
		icon = "language-python",
		pos_hint = {"center_x":0.1, "center_y":0.2},
		on_release = self.py
		)

		tele2 = MDFloatingActionButton(
		icon = "telegram",
		pos_hint = {"center_x": 0.1, "center_y": 0.1},
		on_release = self.teleg,)
		log = MDRoundFlatButton(
		text= "Get",
		pos_hint = {"center_x":0.5,"center_y":0.4},
		text_color = (0, 1, 0, 1),
		font_size = 60,
		on_press = self.login
		)
		self.screen.add_widget(self.id)
		self.screen.add_widget(self.token)
		self.screen.add_widget(python)
		self.screen.add_widget(tele2)
		self.screen.add_widget(self.user)
		self.screen.add_widget(log)
		self.screen.add_widget(an)
		self.screen.add_widget(insta)
		return self.screen
	def py(self,nd):
		webbrowser.open("https://t.me/Pydroi_D")
	def teleg(self,hs):
		webbrowser.open("https://t.me/freefollowers7")
	def instagram(self,sjd):
		webbrowser.open("https://instagram.com/ehq_m")
	def login(self,shd):
		if self.token.text=="" or self.id.text=="":
			error = "ERROR ENTER TOKEN AND ID"
			self.dialog = MDDialog(
			text=error,
			size_hint=(0.8,1),
			buttons=[
			MDFlatButton(
			text="Close",
			on_release=self.close_dialog
			)
			]
			)
		if self.user.text=="":
			error = "ERROR PLEASE ENTER USER"
			self.dialog = MDDialog(
			text=error,
			size_hint=(0.8,1),
			buttons=[
			MDFlatButton(
			text="Close",
			on_release=self.close_dialog
			)
			]
			)
		else:
			user = self.user.text
			token = self.token.text
			id = self.id.text
			he = {
	'accept': '*/*',
	'accept-encoding': 'gzip, deflate, br',
	'accept-language': 'ar',
	'cookie': 'csrftoken=qLKG0H8Y4BavlpaeJLS8mXsbjyaYWUdI;mid=Yw2UXgAEAAE4Z0qqjhY5LAruCxGL;ig_did=581A8852-CB4E-4DCE-8112-8DBD48CFA6DF;ig_nrcb=1',
	'origin': 'https://www.instagram.com',
	'referer': 'https://www.instagram.com/',
	'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
	'sec-ch-ua-mobile': '?0',
	'sec-ch-ua-platform': '"Windows"',
	'sec-fetch-dest': 'empty',
	'sec-fetch-mode': 'cors',
	'sec-fetch-site': 'same-site',
	'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
	'x-asbd-id': '198387',
	'x-csrftoken': 'qLKG0H8Y4BavlpaeJLS8mXsbjyaYWUdI',
	'x-ig-app-id': '936619743392459',
	'x-ig-www-claim': '0',
	}
			urlg = f'https://i.instagram.com/api/v1/users/web_profile_info/?username={user}'
			try:
				re =requests.get(urlg,headers=he).json()
				bio = re["data"]["user"]["biography"]
				followers = re["data"]["user"]["edge_followed_by"]["count"]
				following = re["data"]["user"]["edge_follow"]["count"]
				name = re["data"]["user"]["full_name"]
				id = re["data"]["user"]["id"]
				img = re["data"]["user"]["profile_pic_url"]
				posts = re["data"]["user"]["edge_owner_to_timeline_media"]["count"]
				date = requests.get(f"https://o7aa.pythonanywhere.com/?id={id}").json()["data"]
				m = f"""
• User => {user}
• ID => {id}
• Followers => {followers}
• Following => {following}
• Name => {name}
• Bio => {bio}
• Posts => {posts}
• Date => {date}
• Programmer => @Pydroi_D"""
				requests.get("https://api.telegram.org/bot"+str(self.token.text)+"/sendMessage?chat_id="+str(self.id.text)+"&text="+str(m))
				user_error = m
				self.dialog = MDDialog(
				text=user_error,
				size_hint=(0.8, 1),
				buttons=[
				MDFlatButton(text='Close', on_release=self.close_dialog),

                ]
              )
				self.dialog.open()
			except requests.exceptions.RequestException as e:
				error = "ERROR USER"
				self.dialog = MDDialog(
				text=error,
				size_hint=(0.8,1),
				buttons=[
				MDFlatButton(
				text="Close",
				on_release=self.close_dialog
			)
			]
			)
		self.dialog.open()
	def close_dialog(self,skf):
		self.dialog.dismiss()
Hamody().run()
