<template>

<!-- Navbar -->
  <nav class="navbar navbar-expand-md navbar-light mx-2 px-2">
    <div class="container">
      <!-- navbar brand / title -->
      <div class="navbar-brand">
        <span class=" fw-bold">
          <router-link to='/'>Sohochor</router-link>
          
        </span>
      </div>
      <!-- toggle button for mobile nav -->
      <button
      class="navbar-toggler"
      type="button"
      data-mdb-toggle="collapse"
      data-mdb-target="#main-nav"
      aria-controls="main-nav"
      aria-expanded="false"
      aria-label="Toggle navigation"
    >
      <i class="fas fa-bars"></i>
    </button>

      <!-- navbar links -->
      <div class="collapse navbar-collapse justify-content-end align-center" id="main-nav">
        <ul class="navbar-nav">
          <li v-if="this.$store.state.user !== null" class="nav-item px-2 me-1 py-3">
            <b>Hi! {{$store.state.user.username}} 🙋</b> 
          </li>
          <li v-if="this.$store.state.user !== null" class="nav-item px-2 me-1 py-3">
            <router-link to='/ticket'><b>Ticket</b></router-link>
          </li>
          
          
          <li v-if="this.$store.state.user !== null" class="nav-item px-2 me-1 py-3">
            <router-link to='/apply'><b>Apply for 50% off</b></router-link>
          </li>
          <li class="nav-item px-2 me-1 py-3">
            <router-link to='/about'><b>About</b> </router-link>
          </li>
          <li class="nav-item px-2 me-1 py-3">
            <router-link to='/staffInfo'><b>Staff info</b> </router-link>
          </li>
          <li v-if="this.$store.state.user !== null" class="nav-item px-2 me-1 py-2">
            <button v-on:click='logout' class="btn btn-primary">Log out</button>
          </li>
          <li v-if='this.$store.state.user === null' class="nav-item px-2 me-1 py-2">
            <router-link to='/login'>
            <button class="btn btn-primary">Login</button>
            </router-link>
          </li>

          
          
          
        </ul>
      </div>
    </div>
  </nav>
<!-- Navbar -->

  
  
  
          
  <router-view/>
</template>

<script>
import axios from 'axios'
export default {
  async created(){
    console.log('create from app')
    
    await axios.get('api/auth/users/me/')
    .then(res => {
      this.$store.dispatch('user',res.data)
      console.log(this.$store.state.user)

    })
    .then(err =>{
      console.log(err)
    })

    
  },
  methods:{
    async logout(){
      await axios.post('api/auth/token/logout')
      .then(res => {
        console.log(res)
        localStorage.removeItem('token')
        this.$store.dispatch('user',null)
        this.$router.push('/')
      })
      .then(err => {
        console.log(err)
      })
    }
    
      
    
  }
}
</script>

<style >
.navbar-brand{
  font-size: 1.5rem;
  font-weight: 900;
  
}

.navbar{
  background-color:  #F6F5F5;
}

body{
  background-color: #FEFBF3;
}

.btn-success{
  background-color: #4E9F3D;
}

a{
  color: Black;
}

</style>>





