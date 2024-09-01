from ale_utils import scores as ale_scores
from ale_utils import basics
import statistics
from pdb import set_trace

def compute_partial_hns_scores(alg_scores):
	alg_envs = list(alg_scores.keys())
	assert all([env in basics.ATARI_57 for env in alg_envs])
	hns = {}
	for env in alg_envs:
		hns[env] = (alg_scores[env] - ale_scores.RND_SCORES_ATARI_57[env]) / (ale_scores.HUMAN_SCORES_ATARI_57[env] - ale_scores.RND_SCORES_ATARI_57[env])
	return hns

def compute_hns_scores(alg_scores):
	alg_envs = list(alg_scores.keys())
	assert all([env in alg_envs for env in basics.ATARI_57])
	return compute_partial_hns_scores(alg_scores)

def get_hns_statistics(hns_scores, stat):
	assert stat in ['mean', 'median', 'mode', 'iqm']
	sorted_hns_scores = sorted(list(hns_scores.values()))
	if stat == 'mean':
		return statistics.mean(sorted_hns_scores)
	elif stat == 'median':
		return statistics.median(sorted_hns_scores)
	elif stat == 'mode':
		return statistics.mode(sorted_hns_scores)
	else:
		cut_points = statistics.quantiles(sorted_hns_scores, n=4)
		q1, q3 = cut_points[0], cut_points[2]
		iqr_data = [hns for hns in sorted_hns_scores if q1 <= hns <= q3]
		iqm = statistics.mean(iqr_data)
		return iqm

if __name__ == '__main__':
	hns_scores = compute_hns_scores(ale_scores.HUMAN_SCORES_ATARI_57) # should be ones
	get_hns_statistics(hns_scores, 'iqm')

