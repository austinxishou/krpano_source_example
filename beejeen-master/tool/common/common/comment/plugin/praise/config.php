<?php
/*
 * 点赞插件
*/

$plugins['praise'] = array(
		'plugin_name' => '隐藏点赞',
		"enable" => 1,    			
		"edit_container" => "option_group",
		"edit_sort" => 8,
		"view_container" => "right_bottom",
		"view_sort" => 4,
		"table"=>"worksmain",
  		"column"=>"hidepraise_flag"
	);


?>