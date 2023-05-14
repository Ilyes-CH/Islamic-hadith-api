const button = document.querySelector('.btn');
const dataspace = document.querySelector('.space');


button.addEventListener('click',()=>{
    fetch('/api/data')
    .then(res=>{
        if(!res.ok){
            throw new Error('not 200')
        }
        return res.json();
    })
    .then(data=>{
        
        console.log(data);
        dataspace.textContent+= 'Data in the Console'})
    .catch(err =>{
        console.err('ERROR ',err)
    })
    });