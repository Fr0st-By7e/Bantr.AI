# Chatting interface for 3 characters using Tkinter
import tkinter as tk
from tkinter import ttk, scrolledtext
from PIL import Image, ImageTk
import os
from companions import chat_Cinema_Rasigan, chat_Sharma_ji_ka_Beta, chat_Sporty_Chettan

COMPANIONS = {
	"Sharma-ji ka Beta": {
		"avatar": "Companion_Avatars/Sharma-ji_ka_Beta.png",
		"chat_func": chat_Sharma_ji_ka_Beta
	},
	"Cinema Rasigan": {
		"avatar": "Companion_Avatars/Cinema_Rasigan.png",
		"chat_func": chat_Cinema_Rasigan
	},
	"Sporty Chettan": {
		"avatar": "Companion_Avatars/Sporty_Chettan.png",
		"chat_func": chat_Sporty_Chettan
	}
}

class ChatApp:
	def __init__(self, root):
		self.root = root
		self.root.title("AI Companion Chat")
		self.root.geometry("500x600")

		self.selected_companion = tk.StringVar(value=list(COMPANIONS.keys())[0])
		self.avatar_img = None

		# Companion selection
		top_frame = tk.Frame(root)
		top_frame.pack(pady=10)
		tk.Label(top_frame, text="Select Companion:").pack(side=tk.LEFT)
		self.companion_menu = ttk.Combobox(top_frame, textvariable=self.selected_companion, values=list(COMPANIONS.keys()), state="readonly")
		self.companion_menu.pack(side=tk.LEFT, padx=5)
		self.companion_menu.bind("<<ComboboxSelected>>", self.update_avatar)

		# Avatar display
		self.avatar_label = tk.Label(root)
		self.avatar_label.pack(pady=5)
		self.update_avatar()

		# Chat history
		self.chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, state='disabled', width=60, height=20)
		self.chat_area.pack(padx=10, pady=10)

		# User input
		input_frame = tk.Frame(root)
		input_frame.pack(pady=5)
		self.user_entry = tk.Entry(input_frame, width=40)
		self.user_entry.pack(side=tk.LEFT, padx=5)
		self.user_entry.bind('<Return>', self.send_message)
		send_btn = tk.Button(input_frame, text="Send", command=self.send_message)
		send_btn.pack(side=tk.LEFT)

	def update_avatar(self, event=None):
		companion = self.selected_companion.get()
		avatar_path = COMPANIONS[companion]["avatar"]
		if os.path.exists(avatar_path):
			img = Image.open(avatar_path).resize((80, 80))
			self.avatar_img = ImageTk.PhotoImage(img)
			self.avatar_label.config(image=self.avatar_img)
		else:
			self.avatar_label.config(image=None, text="[No Avatar]")

	def send_message(self, event=None):
		user_msg = self.user_entry.get().strip()
		if not user_msg:
			return
		companion = self.selected_companion.get()
		chat_func = COMPANIONS[companion]["chat_func"]
		self.append_chat("You", user_msg)
		self.user_entry.delete(0, tk.END)
		self.root.after(100, self.get_ai_response, chat_func, user_msg, companion)

	def get_ai_response(self, chat_func, user_msg, companion):
		try:
			ai_msg = chat_func(user_msg)
		except Exception as e:
			ai_msg = f"[Error: {e}]"
		self.append_chat(companion, ai_msg)

	def append_chat(self, sender, message):
		self.chat_area.config(state='normal')
		self.chat_area.insert(tk.END, f"{sender}: {message}\n")
		self.chat_area.see(tk.END)
		self.chat_area.config(state='disabled')


if __name__ == "__main__":
	root = tk.Tk()
	app = ChatApp(root)
	root.mainloop()
