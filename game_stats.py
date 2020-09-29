# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 05:06:56 2018

@author: erikm
"""

class GameStats():
    """Track statistics for Alien Invasion."""
    
    def __init__(self, ai_settings):
        """Initialize statistics."""
        self.ai_settings = ai_settings
        self.reset_stats()
        
        # Start Alien Invasion in an inactive state.
        self.game_active = False
        self.game_pause = False
        
        # High score should never be reset
        self.high_score = 0
        
    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
        
    