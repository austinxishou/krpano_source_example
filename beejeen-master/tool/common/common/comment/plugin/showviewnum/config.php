<?php
/*
 * 隐藏人气插件
*/

$plugins['showviewnum'] = array(
		'plugin_name' => '隐藏人气',
		"enable" => 1,    			
		"edit_container" => "option_group",
		"edit_sort" => 5,
		"view_container" => "left_top",
		"view_sort" => 3,
		"view_resource"=>1,
		"table"=>"worksmain",
  		"column"=>"hideviewnum_flag"
	);


?>