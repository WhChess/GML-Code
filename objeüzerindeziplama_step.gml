y+= dikey_hiz;

if(!place_meeting(x, y+1, obj_duvar)){
	dikey_hiz += yercekimi
}
	
	
if(place_meeting(x, y+dikey_hiz, obj_duvar)){
	while(!place_meeting(x, y+sign(dikey_hiz), obj_duvar)){
		y += sign(dikey_hiz);
	}
	dikey_hiz = 0;
}
if(place_meeting(x,y,obj_zip)){
	dikey_hiz = -10;
}