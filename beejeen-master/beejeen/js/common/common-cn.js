function search( search ){
	
	$.ajax({
	    url:'http://www.beejeen.com/index?key=' + search,
	    type:'get',
	    async:true,
	    timeout:5000,
	    dataType:'json',
	    success:function(data,textStatus,jqXHR){
	    	console.log(data)
	        console.log(textStatus)
	        console.log(jqXHR)
			if(!!data.link){
				location.href=data.link.replace('.html','-cn.html');
			}else{
			 	alert('您搜索的内容不存在');
			}
	   }
	});
}
