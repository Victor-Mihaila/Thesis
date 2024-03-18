The code and data in this repository reproduce the figures showing the results of my Bachelor's thesis.

- `calphas` contains the script `plot_roc_calphas.py` which produces the ROC1 plots for the SCOPe40 sensitivty benchmark, at the level of family, superfamily and fold, for Foldseek translating sequences from PDB files or predicting them using ProstT5, in both cases including C-alpha information or not
- `query_target` contains the script `plot_roc.py` which  ROC1 plots for the SCOPe40 sensitivty benchmark at the level of superfamily for Foldseek ran with all possible combinations of ProstT5/PDB query/target databases
- `jac_cpu` contains the jupyter notebook `identity_visualization.ipynb` which produces the figures that prove the use of evolutionary information in ProstT5 through the Categorical Jacobian calculation described in the thesis and displays an analysis of the identity percentages between translated/predicted 3Di sequences and profiles. The first part of the notebook is based on the method presented in https://github.com/zzhangzzhang/pLMs-interpretability/blob/main/jac/01_jac_calculate_visualise.ipynb
