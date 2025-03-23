from typing import Callable, Any
import pygame

class Timer:
    @staticmethod
    def after(delay: float, callback: Callable, *args: Any) -> None:
        pygame.time.set_timer(pygame.USEREVENT, int(delay * 1000), 1) 

        def handler(play_state):
            callback(play_state) 
            pygame.time.set_timer(pygame.USEREVENT, 0)  

        
        def event_handler(event):
            if event.type == pygame.USEREVENT:
                handler(event.play_state) 

        
        event_handler.play_state = args[0] if args else None  

        pygame.event.set_allowed(pygame.USEREVENT)
        
        event = pygame.event.Event(pygame.USEREVENT)
        pygame.event.post(event)




