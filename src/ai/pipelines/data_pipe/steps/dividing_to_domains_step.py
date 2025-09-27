from zenml import step
from typing import List, Dict
from ai.pipelines.data_pipe.utils.llm_chains import domen_segmentation_chain
import time


@step
def dividing_to_domains_step(summary_texts: List[str]):
    """
    Соотносит части информации из текстов с нужными доменами.

    Args:

    Retrurns:

    """

    time.sleep(10)
    segmented = domen_segmentation_chain(summary_texts)

    return segmented
    #     for segment in segmented["segments"]:

    #         if segment["domain"] == 'HeroMechanicsTips':
    #             hero_mechanics_tips.append(segment["text"])

    #         elif segment["domain"] == 'MatchActionsTips':
    #             match_actions.append(segment["text"])

    #         elif segment["domain"] == 'BaseGameMechanics':
    #             base_game_mechanics.append(segment["text"])

    #         elif segment["domain"] == 'ComicStrategies':
    #             comic_strats.append(segment["text"])

    #         else:
    #             error_counter += 1
    #             continue

    # return {
    #     "hero_mechanics_tips": hero_mechanics_tips,
    #     "match_actions": match_actions,
    #     "base_game_mechanics": base_game_mechanics,
    #     "comic_strats": comic_strats,
    #     "error_counter": error_counter
    #     }
