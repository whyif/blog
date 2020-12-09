<template>
  <div id='app'>
    <p>{{greeting}}</p>
    <p>{{flaskgreeting}}</p>
  </div>
</template>

<script>
export default {
  data:function() {
    return {
      greeting:'hello vue!',
      flaskgreeting:''
    }
  },
  created:async function(){
    const getres= await fetch('http://127.0.0.1:5000/administer_data')
    const getobj=await getres.json()
    this.flaskgreeting=getobj.greeting
  }
}
</script>