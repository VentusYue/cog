import h5py
import os

DATA_PATH = "/home/yue/data/"

def _load_h5_files(self, dir):
    filenames = []
    for root, dirs, files in os.walk(dir):
        for file in files:
            if file.endswith(".h5"): filenames.append(os.path.join(root, file))
    return filenames

# def _get_raw_data(self, index):
#         data = AttrDict()
#         file_index = index // self.samples_per_file
#         path = self.filenames[file_index]

#         try:
#             with h5py.File(path, 'r') as F:
#                 ex_index = index % self.samples_per_file  # get the index
#                 key = 'traj{}'.format(ex_index)

#                 # Fetch data into a dict
#                 for name in F[key].keys():
#                     if name in ['states', 'actions', 'pad_mask']:
#                         data[name] = F[key + '/' + name][()].astype(np.float32)

#                 if key + '/images' in F:
#                     data.images = F[key + '/images'][()]
#                 else:
#                     data.images = np.zeros((data.states.shape[0], 2, 2, 3), dtype=np.uint8)
#         except:
#             raise ValueError("Could not load from file {}".format(path))
        
#         return data

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