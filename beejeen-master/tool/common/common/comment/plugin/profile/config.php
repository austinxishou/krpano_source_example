<?php
/*
 * 项目简介插件
*/

$plugins['profile'] = array(
		'plugin_name' => '隐藏项目简介',
		"enable" => 1,    			
		"edit_container" => "option_group",
		"edit_sort" => 7,
		"view_container" => "right_bottom",
		"view_sort" => 3,
		"view_resource"=>1,       //是否加载了其他资源 比如弹框等
		"table"=>"worksmain",
  		"column"=>"hideprofile_flag"
	);


?>