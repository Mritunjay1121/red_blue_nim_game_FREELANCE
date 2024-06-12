import sys
import math
try:
    def evaluate(piles):
        return 2*piles["red"]+3*piles["blue"]
    def get_computer_move(piles,depth):
        
        def minmax(node, depth, alpha, beta, maximizing_player):
            if depth == 0 or node['red'] == 0 or node['blue'] == 0:
                return node['score']
            if maximizing_player:
                max_eval = -math.inf
                for child in get_children(node):
                    eval = minmax(child, depth-1, alpha, beta, False)
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
                return max_eval
            else:
                min_eval = math.inf
                for child in get_children(node):
                    eval = minmax(child, depth-1, alpha, beta, True)
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
                return min_eval

        def get_children(node):
            children = []
            if node['red'] > 0:
                children.append({'red': node['red']-1, 'blue': node['blue'], 'score': node['score'] + 2*node['red']})
            if node['blue'] > 0:
                children.append({'red': node['red'], 'blue': node['blue']-1, 'score': node['score'] + 3*node['blue']})
            return children

        node = {'red': piles['red'], 'blue': piles['blue'], 'score': 0}
        max_score = -math.inf
        
        for child in get_children(node):
            score = minmax(child, depth, -math.inf, math.inf, False)
            if score > max_score:
                max_score = score
                best_move = {'red': node['red']-child['red'], 'blue': node['blue']-child['blue']}
        piles['red'] -= best_move['red']
        piles['blue'] -= best_move['blue']
        return piles
        
    def get_human_move(piles):
        while True:
            
            pile=input(f'Enter pile to be choosen from human ')

            if (pile.isdigit()==True) or (pile !="red" and pile!="blue"):
                print("Choose btw 'red' or 'blue'")
                continue
            print("Before human processing we have state: ",piles)
            if pile=='red':
                piles['red']-=1
                break
            elif pile=='blue':
                piles['blue']-=1
                break
        return piles
        
    def red_blue_nim(red_val,blue_val,first_player,depth):
        piles={'red':red_val,'blue':blue_val}
        print()
        print(f'Starting red_blue_nim game with {piles["red"]} red marbles and {piles["blue"]} blue marbles')
        print()
        while True:
            if first_player=="human":
                if piles['red']==0:
                    return f"Red already 0 so Human won with final_score: {evaluate(piles)}"
                elif piles['blue']==0:
                    return f"Blue already 0 so Human won with final_score: {evaluate(piles)}"
                piles = get_human_move(piles)
                print("After processing Human's turn we got: ",piles)
                print()

            elif first_player=="computer": 

                print("First player Computer so it is being processed")
                if piles['red']==0:
                    return f"Red already 0 so Computer won with final_score: {evaluate(piles)}"
                elif piles['blue']==0:
                    return f"Blue already 0 so Computer won with final_score: {evaluate(piles)}"
                
                prev_red=piles['red']
                prev_blue=piles['blue']
                print("Before processing Computer's turn we got: ",piles)
                piles=get_computer_move(piles,depth)
               
                after_red=piles['red']
                after_blue=piles['blue']
                if prev_red>piles['red']:
                    print("Computer have chosen red marble")
                    print("After processing Computer's turn we got: ",piles) 
                    print()
                elif prev_blue>piles['blue']:
                    print("Computer have chosen blue marble ")
                    print("After processing Computer's turn we got: ",piles) 
                    print()
            else:
                print("Choose between 'computer' or 'human' ")
                break
                
            break
            
        
        prev_player=first_player
        while True:
            if prev_player=="computer":
                if piles['red']==0:
                    return f"Red already 0 so Human won with final_score: {evaluate(piles)}"
                elif piles['blue']==0:
                    return f"Blue already 0 so Human won with final_score: {evaluate(piles)}"
                piles=get_human_move(piles)
                print("After processing Human's turn we got: ",piles)
                print()

                current_player="human"
            elif prev_player=="human":

                            
                if piles["red"]==0:
                    return f"Red already 0 so Computer won with final_score: {evaluate(piles)}"
                elif piles["blue"]==0:
                    return f"Blue already 0 so Computer won with final_score: {evaluate(piles)}"
                print("Present player Computer so it is being processed")
                print("Before processing Computer's turn we got: ",piles)
                   
                
                prev_red=piles['red']
                prev_blue=piles['blue']
                piles=get_computer_move(piles,depth)
                if prev_red>piles['red']:
                    print("Computer have chosen red marble ")
                    print("After processing Computer's turn we got: ",piles) 
                    print()
                if prev_blue>piles['blue']:
                    print("Computer have chosen blue marble ")
                    print("After processing Computer's turn we got: ",piles) 
                    print()
                
                
                
                current_player="computer"
                
            
            prev_player,current_player=current_player,prev_player
                
                
                
                
    if __name__ == "__main__":
        num_red = int(sys.argv[1])
        num_blue = int(sys.argv[2])
        first_player=str(sys.argv[3])
        depth=int(sys.argv[4])
        print(red_blue_nim(num_red,num_blue,first_player,depth))
except:
    pass

