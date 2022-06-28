from normal_distribution import normal_dist


if __name__ == "__main__":

    #----  reading data
    # Normal Distribution
    mean = 20 
    sd = 2
    norm_dist = normal_dist(mean, sd)
    print(f'\nNormal Distribution:   mean={norm_dist.get_mean()},  standard deviation={norm_dist.get_stdev()}')
