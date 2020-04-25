import utils
import save_arrays
import sys

if __name__ == '__main__':
    name = "goals"
    read_folder, save_path = utils.get_folders(sys.argv, name)
    plans = utils.get_plans(read_folder)
    goals = []
    for p in plans:
        if p.goals not in goals:
            goals.append(p.goals)
    save_arrays.save(goals, save_path)
    print(len(goals))

