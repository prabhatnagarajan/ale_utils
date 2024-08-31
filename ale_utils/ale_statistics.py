from ale_utils import scores as ale_scores
from ale_utils import basics
from pdb import set_trace

def compute_hns_scores(alg_scores):
	hns = {}
	for env in basics.ATARI_57:
		hns[env] = (alg_scores[env] - ale_scores.RND_SCORES_ATARI_57[env]) / (ale_scores.HUMAN_SCORES_ATARI_57[env] - ale_scores.RND_SCORES_ATARI_57[env])
	return hns

def get_hns_statistics(hns_scores, stat='median'):
	assert stat in ['mean', 'median', 'mode']

if __name__ == '__main__':
	compute_hns_scores(ale_scores.HUMAN_SCORES_ATARI_57) # should be ones
