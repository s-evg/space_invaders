class Stats():
    """Отслеживание статистики игры"""

    def __init__(self):
        """Инициализация статистики"""
        self.reset_stats()
        self.run_game = True
        with open('highscore', 'r') as f:
            self.high_score = int(f.read())

    def reset_stats(self):
        """Статистика, изменяющаяся во время игры"""
        self.guns_life = 5
        self.score = 0
