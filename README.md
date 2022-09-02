![GreyBrickBuildings](figures/greybricks_visio.png)

# Grey-brick buildings

This repository presents Grey-brick buildings, an open source data set of 225 calibrated Dutch residential building heat models, comprising identified models and their respective forward selection paths, estimated RC parameters, building thermal properties, i.e., heat transfer coefficient, as well as reported building meta-data.

The results are founded on the method of the open-access journal article [Fifty shades of grey: Automated stochastic model identification of building heat dynamics](https://doi.org/10.1016/j.enbuild.2022.112095).

## Publications or Projects that use Grey-brick Buildings data-set
Please update this list if you use Grey-birck buildings in your work. Naming convention is a number (for ordering), the creator's initials, and a short `-` delimited description, e.g. `1.0-jl-demand-side-management`.

- (publication here)


### Citation
If you find this dataset useful and use it in your work, please reference our article:

[Leprince, J., Miller, C., Madsen, H., Basu, K., Van der Clist, R., and Zeiler, W., 2022. Grey-brick buildings, an open data set of calibrated RC models of Dutch residential building heat dynamics. Energy and Buildings, p.112095.](https://doi.org/10.1016/j.enbuild.2022.112095)

```

```

## Repository structure
```
fiftyshadesofgrey
└─ data
|   ├─ calibrated_models                <- final identified models with calibrated parameters
|   ├─ forward_selection_paths          <- selected path of final identified models
|   ├─ meta_data                        <- self-reported building characteristic meta-information
|   └─ nCPBES                           <- calculated nCPBES of final identified models
├─ figures                              <- obtained figures from data files
└─ README.md                            <- README for developers using this code
```

## Authors

[Julien Leprince](https://github.com/JulienLeprince),
Prof. [Clayton Miller](https://github.com/cmiller8),
Prof. [Henrik Madsen](https://henrikmadsen.org/),
Dr. [Kaustav Basu](https://www.linkedin.com/in/kaustav-basu-phd-5973311b/),
[Rik van der Vlist](https://www.linkedin.com/in/rik-van-der-vlist-124b62138/),
Prof. [Wim Zeiler](https://www.tue.nl/en/research/researchers/wim-zeiler/).


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details