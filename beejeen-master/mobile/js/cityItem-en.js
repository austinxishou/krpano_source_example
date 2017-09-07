var data_response='';
	
$(function(){

	request( location.search.replace('?','') );

});

function request(request){
    $.ajax({
	    url:'http://m.beejeen.com/cityitem?' + request,
	    type:'get',
	    async:true,
	    timeout:5000,
	    dataType:'json',
	    beforeSend:function(xhr){
	        console.log(xhr)
	        console.log('发送前')
	    },
	    success:function(data,textStatus,jqXHR){
	        console.log('成功')
	        console.log(data)
	        console.log(textStatus)
	        console.log(jqXHR)
	        data_response=data;
			if(!!data.link){
				location.href=data.link.replace('.html','-en.html');
			}else{
			 	apppend_data(data.item,'body>main');
			}
	    },
	    error:function(xhr,textStatus){
	        console.log('错误')
	        console.log(xhr)
	        console.log(textStatus)
	    },
	    complete:function(){
	        console.log('结束')
	    }
  	});
}

function apppend_data(data,position){
	
	var html = '';
	
	if( data.length > 0 ){
		
		var type = data[0].table ;
		
		for ( var i =0 ; i < data.length ; i++ ) {
			html += '<a href="tour.html?'+type+'&key='+data[i].name+'">';
			html += '<div style="background-image: url('+data[i].img+');">';
			html += '<h3>'+data[i].name+'</h3>';
			html += '</div>';
			html += '</a>';
		}
		
	}else{
		html = '<h3>Please waiting</h3>' ;
	}
	
	$(position).html(html);
}
	
		
