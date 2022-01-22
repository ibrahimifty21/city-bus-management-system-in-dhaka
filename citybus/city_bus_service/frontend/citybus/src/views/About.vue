<template>
  
  <div class="container">
    <div class="row mt-3">
      <div v-for="blog in blogs" :key="blog.id" class="col-lg-4 col-md-6 my-3">
        <router-link :to="{name:'BlogDetails',params:{id:blog.id}}">
        <div class="card">
          <div class="card-body">
            
            <h5 class="card-title">{{blog.title}}</h5>
           
            
            
              
            
            
            <p class="card-text">
              {{blog.short_description}}
            </p>
            <span><small class="muted">{{blog.created}}</small></span>
          </div>
        

        
        
          
        
      </div>
       </router-link>
    </div>
  </div>
  </div>
  <router-view></router-view>
</template>
<script>
import axios from 'axios'
export default {
  data(){
    return{
      blogs:[]
    }
  },
  async mounted() {
    delete  axios.defaults.headers.common["Authorization"];
    await axios.get('api/blog/')
    .then(res => {
      this.blogs = res.data
      axios.defaults.headers.common['Authorization'] =  "Token "  +  localStorage.getItem('token')
    })
    .then(err => {
      console.log(err)
    })
  },
}
</script>
<style>
.navbar-brand{
  font-size: 1.5rem;
  font-weight: 900;
  
}

.navbar{
  background-color:  #F6F5F5;
}
</style>