console.log("Done")
let theme = localStorage.getItem('theme')

if(theme == null){
	setTheme('light')
}
else{
	setTheme(theme)

}
let themeDots = document.getElementsByClassName('theme-dot')
console.log(themeDots)

for(var i=0; themeDots.length > i; i++){
	themeDots[i].addEventListener('click', function(){
		console.log("Clicked")
		let mode = this.dataset.mode
		console.log("Clicked", mode)
		setTheme(mode)

	})
}

function setTheme(mode){
	if(mode == 'light'){
		document.getElementById('theme-style').href = static + '/default.css'
	}

	if(mode == 'blue'){
		document.getElementById('theme-style').href = static + '/blue.css'
	}

	if(mode == 'purple'){
		document.getElementById('theme-style').href = static + '/purple.css'
	}

	if(mode == 'green'){
		document.getElementById('theme-style').href = static + '/green.css'
	}

	localStorage.setItem('theme', mode)
}