import h5py
import os

DATA_PATH = "/home/yue/data/"

def _load_h5_files(self, dir):
    filenames = []
    for root, dirs, files in os.walk(dir):
        for file in files:
            if file.endswith(".h5"): filenames.append(os.path.join(root, file))
    return filenames

def main(args):
    data = []
    for i in range():
        traj = dict(
            observations=[],
            actions=[],
            rewards=[],
            next_observations=[],
            terminals=[],
            agent_infos=[],
            env_infos=[],
        )

        with h5py.File(path, 'r') as F:
            key = 'traj01'
            # Fetch data into a dict
            for name in F[key].keys():
                import pdb; pdb.set_trace()
                # if name == "states":
                    
                # elif: name == 'actions':
                
                # elif name == 'pad_mask':



        data.append(traj)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--save-directory", type=str, default=DATA_PATH),
    args = parser.parse_args()

    main(args)