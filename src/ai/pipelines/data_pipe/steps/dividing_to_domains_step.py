from zenml import step
from typing import List, Tuple
from ai.pipelines.data_pipe.utils.llm_chains import domen_segmentation_chain
import time


@step
def dividing_to_domains_step(summary_texts: List[str]) -> List[list]:
    """
    Соотносит части информации из текстов с нужными доменами.
    """
    hero_mechanics_tips = []
    match_actions = []
    base_game_mechanics = []
    comic_strats = []
    error_counter = 0

    for text in summary_texts:
        time.sleep(10)
        if not text:
            continue
        segmented = domen_segmentation_chain(text)
        for segment in segmented["segments"]:

            if segment["domain"] == 'HeroMechanicsTips':
                hero_mechanics_tips.append(segment["text"])

            elif segment["domain"] == 'MatchActionsTips':
                match_actions.append(segment["text"])

            elif segment["domain"] == 'BaseGameMechanics':
                base_game_mechanics.append(segment["text"])

            elif segment["domain"] == 'ComicStrategies':
                comic_strats.append(segment["text"])

            else:
                error_counter += 1
                continue

    return [hero_mechanics_tips, match_actions, base_game_mechanics, comic_strats, error_counter]
