![GreyBrickBuildings](figures/greybricks_visio.png)

# Grey-brick buildings

This repository presents Grey-brick buildings, an open source data set of 225 calibrated Dutch residential building heat models, comprising identified models and their respective forward selection paths, estimated RC parameters, building thermal properties, i.e., heat transfer coefficient, as well as reported building meta-data.

The results are founded on the method of the open-access journal article [Fifty shades of grey: Automated stochastic model identification of building heat dynamics](https://doi.org/10.1016/j.enbuild.2022.112095).


### Citation
If you find this dataset useful and use it in your work, please reference our article:

[Leprince, J., Miller, C., Madsen, H., and Zeiler, W., 2022. Grey-brick buildings, an open data set of calibrated RC models of Dutch residential building heat dynamics. Energy and Buildings, p.112095.](https://doi.org/10.1016/j.enbuild.2022.112095)

```

@article{LEPRINCE2022112095,
title = {Fifty shades of grey: Automated stochastic model identification of building heat dynamics},
journal = {Energy and Buildings},
volume = {266},
pages = {112095},
year = {2022},
issn = {0378-7788},
doi = {https://doi.org/10.1016/j.enbuild.2022.112095},
url = {https://www.sciencedirect.com/science/article/pii/S0378778822002663},
author = {Julien Leprince and Henrik Madsen and Clayton Miller and Jaume Palmer Real and Rik {van der Vlist} and Kaustav Basu and Wim Zeiler},
keywords = {Buildings, Automation, Grey-box models, Heat dynamics, Scalable approaches, Performance benchmarks},
abstract = {To reach the carbon emission reduction targets set by the European Union, the building sector has embraced multiple strategies such as building retrofit, demand side management, model predictive control and building load forecasting. All of which require knowledge of the building dynamics in order to effectively perform. However, the scaling-up of building modelling approaches is still, as of today, a recurrent challenge in the field. The heterogeneous building stock makes it tedious to tailor interpretable approaches in a scalable way. This work puts forward an automated and scalable method for stochastic model identification of building heat dynamics, implemented on a set of 247 Dutch residential buildings. From established models and selection approach, automation extensions were proposed along with a novel residual auto-correlation indicator, i.e., normalized Cumulated Periodogram Boundary Excess Sum (nCPBES), to classify obtained model fits. Out of the available building stock, 93 building heat dynamics models were identified as good fits, 95 were classified as close and 59 were designed as poor. The identified model parameters were leveraged to estimate thermal characteristics of the buildings to support building energy benchmarking, in particular, building envelope insulation performance. To encourage the dissimination of the work and assure reproducibility, the entire code base can be found on Github along with an example data set of 3 anonymized buildings. The presented method takes an important step towards the automation of building modeling approaches in the sector. It allows the development of applications at large-scale, enhancing building performance benchmarks, boosting city-scale building stock scenario modeling and assisting end-use load identifications as well as building energy flexibility potential estimation.}
}

```

## Repository structure
```
fiftyshadesofgrey
└─ data
|   ├─ foward_selection_paths           <- selected path of final identified models
|   ├─ nCPBES                           <- calculated nCPBES of final identified models
|   └─ RCmodels                         <- fitted models with calibrated parameters
└─ README.md                            <- README for developers using this code
```



## Authors

[Julien Leprince](https://github.com/JulienLeprince),
Prof. [Clayton Miller](https://github.com/cmiller8),
Prof. [Henrik Madsen](https://henrikmadsen.org/),
Prof. [Wim Zeiler](https://www.tue.nl/en/research/researchers/wim-zeiler/).


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details