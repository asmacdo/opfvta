def float_to_tex(f,
	max_len=4,
	condensed=False,
	padding=False,
	):
	"""Reformat float to tex syntax
	Parameters
	----------
	f : float
		Float to format.
	max_len : int
		Maximum digit length of output strings.
	"""
	if condensed:
		model_str="{}\\!\\times\\!10^{{{}}}"
	else:
		model_str="{} \\times 10^{{{}}}"


	if f >= 10**-max_len and f <= 10**max_len:
		if f < -1 or f > 1:
			f_str_template = "{{:.{}g}}".format(max_len)
		if f >= -1 and f <= 1:
			f_str_template = "{{:.{}g}}".format(2)
		f_str = f_str_template.format(f)
	else:
		f_str = "{:e}".format(f)
		try:
			f_decimals, f_exponent = f_str.split("e")
		except ValueError:
			return '${}$'.format(f_str)
		truncated_decimals = f_decimals[:max_len].rstrip('.')
		f_str = model_str.format(truncated_decimals,int(f_exponent))
	if padding:
		return '$'+f_str+'$'
	return f_str

def inline_anova(anova,
	factor=None,
	style="python",
	max_len=4,
	condensed=False,
	pythontex_safe=False,
	):
	"""Typeset factor summary from statsmodels-style anova DataFrame for inline mention.

	Parameters
	----------
	df : pandas.DataFrame or statsmodels.ContrastResults
		Pandas DataFrame object containing an ANOVA summary, or Statsmodels ContrastResults object containing an F-contrast.
	factor : str, optional
		String indicating the factor of interest from the summary given by `df`.
	max_len : int
		Maximum digit length of output strings.
	style : {"python", "tex"}, optional
		What formatting to apply to the string. A simple Python compatible string is returned when selecting "python", whereas a fancier output (decorated with TeX syntax) is returned if selecting "tex".
	"""

	if style == "python":
		try:
			inline = "F({:g},{:g})={:2G}, p={:3G}".format(
				anova["df"][factor],
				anova["df"]["Residual"],
				anova["F"][factor],
				anova["PR(>F)"][factor],
				)
		except TypeError:
			inline = "F({:g},{:g})={:2G}, p={:3G}".format(
				anova.df_num,
				anova.df_denom,
				anova.fvalue[0][0],
				anova.pvalue,
				)
	elif style == "tex":
		if condensed:
			string_template = "$F_{{{},{}}}\!=\!{},\\, p\!=\!{}$"
		else:
			string_template = "$F_{{{},{}}}={},\\, p={}$"
		try:
			degrees_of_freedom = float_to_tex(anova["df"][factor], max_len=max_len)
			degrees_of_freedom_rest = float_to_tex(anova["df"]["Residual"], max_len=max_len)
			f_string = float_to_tex(anova["F"][factor], max_len=max_len, condensed=condensed)
			p_string = float_to_tex(anova["PR(>F)"][factor], max_len=max_len, condensed=condensed)
		except TypeError:
			degrees_of_freedom = float_to_tex(anova.df_num, max_len=max_len)
			degrees_of_freedom_rest = float_to_tex(anova.df_denom, max_len=max_len)
			f_string = float_to_tex(anova.fvalue[0][0], max_len=max_len, condensed=condensed)
			p_string = float_to_tex(float(anova.pvalue), max_len=max_len, condensed=condensed)
		inline = string_template.format(
			degrees_of_freedom,
			degrees_of_freedom_rest,
			f_string,
			p_string,
			)
		if pythontex_safe:
			inline = inline.replace("\\","\\\\")
	return inline

def inline_factor(summary,
	factor=None,
	style="python",
	max_len=2,
	pythontex_safe=False,
	percentile=95,
	unit=''
	):
	"""Typeset factor summary from statsmodels-style summary DataFrame for inline mention.

	Parameters
	----------
	df : pandas.DataFrame or statsmodels.ContrastResults
		Pandas DataFrame object containing an ANOVA summary, or Statsmodels ContrastResults object containing an F-contrast.
	factor : str, optional
		String indicating the factor of interest from the summary given by `df`.
	max_len : int
		Maximum digit length of output strings.
	style : {"python", "tex"}, optional
		What formatting to apply to the string. A simple Python compatible string is returned when selecting "python", whereas a fancier output (decorated with TeX syntax) is returned if selecting "tex".
	"""

	if style == "python":
		# The `max_len` formatting does not take effect due to the `g` string formatter.
		string_template="{{:.{}g}}, CI{{:g}}%=[{{:.{}G}}, {{:.{}G}}]".format(max_len, max_len, max_len)
		inline = "{:g}, CI{:g}%=[{:2G}, {:2G}]".format(
			float(summary.tables[1]['Coef.'][factor]),
			percentile,
			float(summary.tables[1]['[0.025'][factor]),
			float(summary.tables[1]['0.975]'][factor]),
			)
	elif style == "tex":
		# Will not work because SIunitx does not accept math mode in the number fields
		string_template = '\SIci'\
			'{{{{{{:.{}f}}}}}}'\
			'{{{{{{}}}}}}'\
			'{{{{{{}}\%}}}}'\
			'{{{{{{:.{}f}}}}}}'\
			'{{{{{{:.{}f}}}}}}'
		string_template = string_template.format(max_len,max_len,max_len)
		factor_value = float(summary.tables[1]['Coef.'][factor])
		lower_bound = float(summary.tables[1]['[0.025'][factor])
		upper_bound = float(summary.tables[1]['0.975]'][factor])
		inline = string_template.format(
			factor_value,
			unit,
			percentile,
			lower_bound,
			upper_bound,
			)
		if pythontex_safe:
			inline = inline.replace("\\","\\\\")
	elif style == "tex_experimental":
		# Will not work because SIunitx does not accept math mode in the number fields
		string_template = '\SIci{{{}}}{{{}}}{{{}\%}}{{{}}}{{{}}}'
		factor_value = float_to_tex(float(summary.tables[1]['Coef.'][factor]), max_len=max_len)
		lower_bound = float_to_tex(float(summary.tables[1]['[0.025'][factor]), max_len=max_len)
		upper_bound = float_to_tex(float(summary.tables[1]['0.975]'][factor]), max_len=max_len)
		inline = string_template.format(
			factor_value,
			unit,
			percentile,
			lower_bound,
			upper_bound,
			)
		if pythontex_safe:
			inline = inline.replace("\\","\\\\")
	return inline
