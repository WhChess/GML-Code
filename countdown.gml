// Create

sayac = 60;
alarm[0] = 60;

// Alarm 0

if(sayac<=60 and sayac>1){
	sayac-=1;
	alarm[0] = 60;
}
else{
	sayac = "Go!";
}
  
// Draw
  
draw_text(mouse_x+100,mouse_y+100,sayac);
