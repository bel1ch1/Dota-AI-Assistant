from zenml import step
from typing import Dict
import time


@step
def dividing_to_topics_step(domains: Dict[str, list]) -> Dict[list]:
    """
    Разделяет информацию из домена на темы содержащие только 1 главную мысль.

    Args:
        domains (List[list]): Списки с информацией по каждому домену

    Returns:
        List[list]: Списки с топиками по каждому домену.
    """


    hero_mechanics_tips = []
    match_actions = []
    base_game_mechanics = []
    comic_strats = []
    error_counter = 0

    for domain in domains:
        if domain["domain"] == 'HeroMechanicsTips':
            hero_mechanics_tips.append(domain["text"])

        elif domain["domain"] == 'MatchActionsTips':
            match_actions.append(domain["text"])

        elif domain["domain"] == 'BaseGameMechanics':
            base_game_mechanics.append(domain["text"])

        elif domain["domain"] == 'ComicStrategies':
            comic_strats.append(domain["text"])

        else:
            error_counter += 1
            continue
