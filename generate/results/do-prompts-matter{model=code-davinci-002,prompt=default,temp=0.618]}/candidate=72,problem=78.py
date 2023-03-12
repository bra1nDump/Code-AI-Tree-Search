
import sys
import math

def get_n_choose_r(n, r, mod):
	"""
	Returns n choose r modulo mod.
	"""
	assert n >= r
	n_fact = 1
	r_fact = 1
	for i in range(n, n - r, -1):
		n_fact *= i
	for i in range(1, r + 1):
		r_fact *= i
	return (n_fact // r_fact) % mod

def get_n_permute_r(n, r, mod):
	"""
	Returns n permute r modulo mod.
	"""
	assert n >= r
	n_fact = 1
	for i in range(n, n - r, -1):
		n_fact *= i
		n_fact %= mod
	return n_fact % mod

def get_n_permute_r_k_groups(n, r, k, mod):
	"""
	Returns n permute r with k groups modulo mod.
	"""
	return (get_n_permute_r(n, r, mod) * get_n_choose_r(r - 1, k - 1, mod)) % mod

def get_n_permute_r_k_groups_no_adjacent(n, r, k, mod):
	"""
	Returns n permute r with k groups not adjacent modulo mod.
	"""
	return (get_n_permute_r(n, r, mod) * get_n_choose_r(r - 1, k - 1, mod) * get_n_permute_r(k, k, mod)) % mod

def get_n_permute_r_k_groups_no_adjacent_no_repeats(n, r, k, mod):
	"""
	Returns n permute r with k groups not adjacent, not repeating modulo mod.
	"""
	return (get_n_permute_r_k_groups_no_adjacent(n, r, k, mod) * get_n_permute_r(r, r, mod)) % mod

def get_n_permute_r_k_groups_no_adjacent_no_repeats_no_sequential(n, r, k, mod):
	"""
	Returns n permute r with k groups not adjacent, not repeating, not sequential modulo mod.
	"""
	return (get_n_permute_r_k_groups_no_adjacent(n, r, k, mod) * get_n_permute_r(r, r, mod) * get_n_permute_r(k, k, mod)) % mod

def get_n_permute_r_k_groups_no_adjacent_no_repeats_no_sequential_no_same_genre(n, r, k, mod):
	"""
	Returns n permute r with k groups not adjacent, not repeating, not sequential, not same genre modulo mod.
	"""
	return (get_n_permute_r_k_groups_no_adjacent_no_repeats_no_sequential(n, r, k, mod) * get_n_permute_r(k, k, mod)) % mod

def get_n_permute_r_k_groups_no_adjacent_no_repeats_no_sequential_no_same_genre_no_same_song(n, r, k, mod):
	"""
	Returns n permute r with k groups not adjacent, not repeating, not sequential, not same genre, not same song modulo mod.
	"""
	return (get_n_permute_r_k_groups_no_adjacent_no_repeats_no_sequential_no_same_genre(n, r, k, mod) * get_n_permute_r(k, k, mod)) % mod

def get_n_permute_r_k_groups_no_adjacent_no_repeats_no_sequential_no_same_genre_no_same_song_no_same_song_order(n, r, k, mod):
	"""
	Returns n permute r with k groups not adjacent, not repeating, not sequential, not same genre, not same song, not same song order modulo