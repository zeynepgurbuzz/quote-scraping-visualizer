import random
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QComboBox, QHBoxLayout
from PyQt5.QtCore import QTimer

class Card:
    def __init__(self, rank, suit=None):
        self.rank = rank
        self.suit = suit
        self.hidden = True  # Kart gizli başlar

    def __str__(self):
        if self.hidden:
            return "🂠"  # Gizli kart için emoji
        return f"{self.rank}{self.suit}"

def create_deck():
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['♠', '♡', '♢', '♣']  # Suitler
    deck = []
    for rank in ranks:
        for suit in suits:
            deck.append(Card(rank, suit))  # Rank ve suit kombinasyonu
    random.shuffle(deck)
    return deck

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.score = 0

    def add_card(self, card):
        self.hand.append(card)

    def remove_card(self, card):
        self.hand.remove(card)

    def has_rank(self, rank):
        return any(card.rank == rank for card in self.hand)

    def get_pairs(self):
        pairs = {}
        for card in self.hand:
            if card.rank not in pairs:
                pairs[card.rank] = []
            pairs[card.rank].append(card)
        pairs_formed = 0
        for rank, cards in pairs.items():
            if len(cards) == 2:  # 2 kart eşleşmesi
                pairs_formed += 1
        self.score += pairs_formed
        return pairs_formed

    def __str__(self):
        return f"{self.name} (Score: {self.score})"

def deal_cards(deck, players):
    for _ in range(7):
        for player in players:
            card = deck.pop()
            player.add_card(card)

class GoFishGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.players = [Player("Player 1"), Player("Player 2")]
        self.deck = create_deck()
        self.current_player_idx = 0
        self.game_over = False
        deal_cards(self.deck, self.players)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Go Fish')
        self.setGeometry(100, 100, 600, 400)
        layout = QVBoxLayout()

        self.player1_label = QLabel(f'Player 1: {self.players[0].score} pairs', self)
        self.player2_label = QLabel(f'Player 2: {self.players[1].score} pairs', self)

        layout.addWidget(self.player1_label)
        layout.addWidget(self.player2_label)

        self.ask_button = QPushButton('Ask', self)
        self.ask_button.clicked.connect(self.ask_card)
        layout.addWidget(self.ask_button)

        self.rank_combo = QComboBox(self)
        self.update_dropdown()  # Dropdown'u güncelle
        layout.addWidget(self.rank_combo)

        self.show_opponent_button = QPushButton('Show Opponent’s Cards', self)
        self.show_opponent_button.clicked.connect(self.show_opponent_cards)
        layout.addWidget(self.show_opponent_button)

        self.setLayout(layout)

    def update_dropdown(self):
        current_player = self.players[self.current_player_idx]
        self.rank_combo.clear()
        self.rank_combo.addItems([str(card) for card in current_player.hand])  # Kartları dropdown menüsüne ekle

    def ask_card(self):
        if self.game_over:
            return

        rank = self.rank_combo.currentText().split(" ")[0]  # Emoji'yi temizle, sadece rank'i al
        current_player = self.players[self.current_player_idx]
        opponent = self.players[1 - self.current_player_idx]

        if opponent.has_rank(rank):
            for card in opponent.hand:
                if card.rank == rank:
                    current_player.add_card(card)
                    opponent.remove_card(card)
        else:
            card = self.deck.pop()
            current_player.add_card(card)

        current_player.get_pairs()
        self.update_gui()

        self.current_player_idx = 1 - self.current_player_idx
        self.update_dropdown()  # Dropdown'u güncelle
        self.check_game_over()

    def update_gui(self):
        self.player1_label.setText(f'Player 1: {self.players[0].score} pairs')
        self.player2_label.setText(f'Player 2: {self.players[1].score} pairs')

    def check_game_over(self):
        if len(self.players[0].hand) == 0 or len(self.players[1].hand) == 0:
            self.game_over = True
            winner = self.players[0] if self.players[0].score > self.players[1].score else self.players[1]
            self.display_winner(winner)

    def display_winner(self, winner):
        winner_label = QLabel(f'{winner.name} wins with {winner.score} pairs!', self)
        self.layout().addWidget(winner_label)

    def show_opponent_cards(self):
        opponent = self.players[1 - self.current_player_idx]
        for card in opponent.hand:
            card.hidden = False
        self.update_gui()
        QTimer.singleShot(3000, self.hide_opponent_cards)  # 3 saniye sonra kartları gizle

    def hide_opponent_cards(self):
        opponent = self.players[1 - self.current_player_idx]
        for card in opponent.hand:
            card.hidden = True
        self.update_gui()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = GoFishGUI()
    ex.show()
    sys.exit(app.exec_())
