def processGame(events: list[tuple[int, int, int]], H: int) -> list[int]:
    """
    Replays match events in frame order, ensuring simultaneous strikes 
    on the same frame are fully applied before checking for a KO.
    
    Parameters:
    events (list of tuples): (player, frame, attack_value)
    H (int): Starting health points for both players.
    
    Returns:
    list[int]: [player1_hp, player2_hp] clamped to a minimum of 0.
    """
    player1_hp = H
    player2_hp = H

    sorted_events = sorted(events, key=lambda x: x[1])

    i = 0
    n = len(sorted_events)

    while i < n:
        if player1_hp <= 0 or player2_hp <= 0:
            break

        current_frame = sorted_events[i][1]
        
        p1_damage_received = 0
        p2_damage_received = 0

        while i < n and sorted_events[i][1] == current_frame:
            player, frame, attack_value = sorted_events[i]
            if player == 1:
                p2_damage_received += attack_value
            elif player == 2:
                p1_damage_received += attack_value
            i += 1

        player1_hp -= p1_damage_received
        player2_hp -= p2_damage_received

    return [max(0, player1_hp), max(0, player2_hp)]

