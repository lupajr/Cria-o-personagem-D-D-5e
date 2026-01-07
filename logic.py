import random
import uuid

# Configurações de prioridade por classe e bônus por raça
CLASS_PRIORITIES = {
    "Guerreiro": ["FOR", "CON", "DEX", "WIS", "CHA", "INT"],
    "Mago": ["INT", "CON", "DEX", "WIS", "CHA", "FOR"],
    "Ladino": ["DEX", "CON", "INT", "WIS", "CHA", "FOR"],
    "Clérigo": ["WIS", "CON", "FOR", "DEX", "CHA", "INT"]
}

RACE_BONUSES = {
    "Humano": {"FOR": 1, "DEX": 1, "CON": 1, "INT": 1, "WIS": 1, "CHA": 1},
    "Elfo": {"DEX": 2, "INT": 1},
    "Anão": {"CON": 2, "FOR": 2},
    "Meio-Orc": {"FOR": 2, "CON": 1}
}

def roll_stats():
    """Rola 4d6 e descarta o menor valor para cada atributo."""
    stats = []
    for _ in range(6):
        rolls = sorted([random.randint(1, 6) for _ in range(4)], reverse=True)
        stats.append(sum(rolls[:3]))
    return sorted(stats, reverse=True)

def generate_character():
    """Gera um personagem completo com ID único e distribuição otimizada."""
    raca = random.choice(list(RACE_BONUSES.keys()))
    classe = random.choice(list(CLASS_PRIORITIES.keys()))
    
    # Distribuição Inteligente: mapeia os maiores valores para as prioridades da classe
    raw_stats = roll_stats()
    priorities = CLASS_PRIORITIES[classe]
    final_stats = {stat: raw_stats[i] for i, stat in enumerate(priorities)}
    
    # Aplicação de Bônus Raciais
    bonuses = RACE_BONUSES[raca]
    for stat, bonus in bonuses.items():
        if stat in final_stats:
            final_stats[stat] += bonus

    # Cálculo de Modificador de Constituição e HP (Base 10 para nível 1)
    con_mod = (final_stats["CON"] - 10) // 2
    hp = 10 + con_mod

    # Retorno unificado em um único dicionário
    return {
        "id": str(uuid.uuid4()),
        "raca": raca,
        "classe": classe,
        "atributos": final_stats,
        "hp": hp,
        "bonus_aplicados": bonuses
    }