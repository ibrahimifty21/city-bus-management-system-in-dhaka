<template>

  <!-- first section -->
  
  <div class="container">
    <div class="row">
      <div class="col-md-6 col-lg-6 my-5 ">
        <h1 class="display-2">Sohochor</h1>
        <h3 class="display-5 muted">Make your journey safe with us</h3>

        <router-link to="/routes">
          <button class="btn btn-primary">Checkout our pickup point</button>
        </router-link>
        
      </div>

      <!-- animation -->
      <div class="col-md-6 col-lg-6 my-3 center">
        <lottie-player src="https://assets4.lottiefiles.com/packages/lf20_BBOVEK.json"  background="transparent"  speed="1"  style="width: 350px;"  loop  autoplay></lottie-player>
      </div>
    </div>
  </div>

  <!-- ticket-section -->

  
  <section class="bg-light">
    <div class="container">
    <div class="row">
      <h1 class="display-4 text-center my-4">Purchase your ticket</h1>
      <!-- <h2>{{pickup}}</h2> -->
      <span v-if='this.$store.state.user === null' class="info my-3 text-center">
        <i class="fas fa-info-circle"></i>
        <b> You have to be logged in or registered for purchasing ticket</b>
      </span>
      
        <div class="row for-form">
          <div class="col-lg-8">
            <form class="mx-3 px-3">
          <div class="form-group row mb-3">
            
            <input v-model="pickup" @focus="form" type="text" class="form-control " id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="⌨ Type your location">
            <div v-if="model">
              <ul  class="list-group" v-for="name in pick_obj" :key="name.id">
                <li class="list-group-item" @click="set_location(name)">{{name.name_of_route}}</li>
              
              </ul>
            </div>
            
            
          </div>
        </form>

          </div>
        </div>
        <div class="row for-form">
          <div class="col-lg-10">
            <table v-if='table && load===false' class="table align-middle">
              <thead>
                <tr>
                  <th scope="col">Bus</th>
                  <th scope="col">Destination</th>
                  <th scope="col">Time</th>
                  <th scope="col">Confirm</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="des in destination" :key="des.id">
                  
                  <td>
                    <span class="mt-2 mx-2">
                      <i class="fas fa-bus-alt"></i>
                    </span>
                    <b>{{des.name_of_bus}}</b>
                  </td>
                  <td>
                    <span class="mt-2 mx-2">
                            <i class="fas fa-map-marker-alt"></i>
                    </span>
                    <b>{{des.name_of_route}}</b>
                  </td>
                  <td>
                    <span class="mt-2 mx-2">
                      <i class="fas fa-clock"></i>
                    </span>
                    <b>{{des.time}}</b>
                    
                  </td>
                  <td>


                    <button type="button" class="btn btn-primary" data-mdb-toggle="modal" data-mdb-target="#exampleModal">
                      confirm
          </button>

<!-- Modal -->
              <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                <div class="modal-dialog modal-dialog-centered">
                  <div class="modal-content">
                    <div class="modal-header">
                      <h5 class="modal-title text-center" id="exampleModalLabel">Purchase confirmation</h5>
                      <button type="button" class="btn-close" data-mdb-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                      <img
                        src="@/assets/bkash.png"
                        class="img-thumbnail"
                        alt="Hollywood Sign on The Hill"
                        width="70" height="70"
                      />
                      <img
                        src="@/assets/rocket.png"
                        class="img-thumbnail mx-2"
                        alt="Hollywood Sign on The Hill"
                        width="70" height="70"
                      />
                      <img
                        src="@/assets/visa.png"
                        class="img-thumbnail mx-2"
                        alt="Hollywood Sign on The Hill"
                        width="70" height="70"
                      />
                    
                    </div>
                    <div class="modal-footer">
                      <button type="button" class="btn btn-danger" data-mdb-dismiss="modal">Close</button>
                      
                      <button @click="confirm(des.name_of_bus,des.name_of_route,des.time)" v-if='$store.state.user !== null && load===false' class="btn btn-primary">
                      Confirm
                    </button>
                    </div>
                  </div>
                </div>
              </div>


                    <!-- <button @click="confirm(des.name_of_bus,des.name_of_route,des.time)" v-if='$store.state.user !== null && load===false' class="btn btn-primary">
                      Confirm
                    </button> -->
                    
                    <button v-if='$store.state.user === null' class="btn btn-primary" disabled>
                      Confirm
                    </button>

                  </td>
                  
                  
                </tr>
                
                
              </tbody>
            </table>

          




            

            <div v-if='load === true' class="d-flex justify-content-center my-4">
              <div class="spinner-border" role="status">
                <span class="visually-hidden">Loading...</span>
              </div>
            </div>

          </div>
        </div>
        

      </div>

      <!-- end -->

      <!-- destination -->
      
      
      
      
      
    
  </div>
  </section>

  <section >
    <div class="mb-3">
      <Covid />
    </div>
    
  </section>

  <section class="bg-light">
    <div class="mb-3">
      <Review />
    </div>
    
  </section>

  

  <!-- ticket-section-end -->
  
    <!-- Footer -->
<footer class="text-center text-lg-start bg-dark  text-white">
  <!-- Section: Social media -->
  <section
    class="d-flex justify-content-center justify-content-lg-between p-4 border-bottom"
  >
    <!-- Left -->
    <div class="me-5 d-none d-lg-block">
      <span>Get connected with us on social networks:</span>
    </div>
    <!-- Left -->

    <!-- Right -->
    <div>
      <a href="" class="me-4 text-reset">
        <i class="fab fa-facebook-f"></i>
      </a>
      <a href="" class="me-4 text-reset">
        <i class="fab fa-twitter"></i>
      </a>
      <a href="" class="me-4 text-reset">
        <i class="fab fa-google"></i>
      </a>
      <a href="" class="me-4 text-reset">
        <i class="fab fa-instagram"></i>
      </a>
      <a href="" class="me-4 text-reset">
        <i class="fab fa-linkedin"></i>
      </a>
      <a href="" class="me-4 text-reset">
        <i class="fab fa-github"></i>
      </a>
    </div>
    <!-- Right -->
  </section>
  <!-- Section: Social media -->

  <!-- Section: Links  -->
  <section class="">
    <div class="container text-center text-md-start mt-5">
      <!-- Grid row -->
      <div class="row mt-3">
        <!-- Grid column -->
        <div class="col-md-3 col-lg-4 col-xl-3 mx-auto mb-4">
          <!-- Content -->
          <h6 class="text-uppercase fw-bold mb-4">
            <i class="fas fa-gem me-3"></i>Sohochor
          </h6>
          <p>
            Make your journey comfortable with us. Please stay with us and be safe.
          </p>
        </div>
        <!-- Grid column -->

        <!-- Grid column -->
        <div class="col-md-2 col-lg-2 col-xl-2 mx-auto mb-4">
          <!-- Links -->
          <h6 class="text-uppercase fw-bold mb-4">
            Service
          </h6>
          <p>
            <a href="#!" class="text-reset">e-ticket</a>
          </p>
          <p>
            <a href="#!" class="text-reset">metro service</a>
          </p>
          <p>
            <a href="#!" class="text-reset">comfortable journey</a>
          </p>
          
        </div>
        <!-- Grid column -->

        <!-- Grid column -->
        
        <!-- Grid column -->

        <!-- Grid column -->
        <div class="col-md-4 col-lg-3 col-xl-3 mx-auto mb-md-0 mb-4">
          <!-- Links -->
          <h6 class="text-uppercase fw-bold mb-4">
            Contact
          </h6>
          <p><i class="fas fa-home me-3"></i> Sewrapara, Road 12: block A</p>
          <p>
            <i class="fas fa-envelope me-3"></i>
            info@sohochor.com
          </p>
          <p><i class="fas fa-phone me-3"></i> + 017 XXX XXX</p>
          <p><i class="fas fa-print me-3"></i> + 017 XXX XXX</p>
        </div>
        <!-- Grid column -->
      </div>
      <!-- Grid row -->
    </div>
  </section>
  <!-- Section: Links  -->

  <!-- Copyright -->
  <div class="text-center p-4" style="background-color: rgba(0, 0, 0, 0.05);">
    © 2021 Copyright:
    <a class="text-reset fw-bold" href="https://mdbootstrap.com/">Sohochor.com</a>
  </div>
  <!-- Copyright -->
</footer>
<!-- Footer -->
  <router-view></router-view>


  
</template>

<script>
// @ is an alias to /src
import axios from 'axios';
import Review from './Review.vue'
import Covid from './Covid.vue'
export default {
  name: 'Home',
  components:{
    Review,
    Covid
  },
  

  data(){
    return{
      pickup:'',
      table:false,
      pick_obj:[],
      destination:{},
      load:false,
      
      
      
      
      model:false
    }
  },
  watch:{
    pickup: function(value){
      const data = {
        pickup:value
      }
      delete  axios.defaults.headers.common["Authorization"];
      axios.post('api/route_search/',data)
      .then(res => {
        
        this.pick_obj = res.data['data']
        this.table = true
        
        axios.defaults.headers.common['Authorization'] =  "Token "  +  localStorage.getItem('token')
      })
      .then(err => {
        console.log(err)
      })
    },
    
  },
  methods:{
    async created(){
      console.log('created from home')
     
      await axios.get('api/auth/users/me/')
    .then(res => {
      this.$store.dispatch('user',res.data)
      console.log(this.$store.state.user)

    })
    .then(err =>{
      console.log(err)
    })

    
    },
    async set_location(value){
      this.pickup = value.name_of_route
      this.model = false
      
      delete  axios.defaults.headers.common["Authorization"];
      const data = {
        bus_id : value.bus_id,
        serial_number: value.station_serial,
        trip_number : value.trip_number
      }
      await axios.post('api/route_search_destination/',data)
      .then(res => {
        
        console.log(res.data['data'])

        this.destination = res.data['data']
        console.log(this.destination)
        axios.defaults.headers.common['Authorization'] =  "Token "  +  localStorage.getItem('token')
      })
      .catch(err => {
        console.log(err)
      })


    },
    
    form(){
      this.model= true
      
    },
    submit(){
      console.log('click')
      
    },
    confirm(busname,destination,time){
      this.load = true
      const data = {
        user:this.$store.state.user.id,
        pickup:this.pickup,
        busname:busname,
        destination:destination,
        time:time
      }
      console.log(data)
      axios.post('api/ticket/',data)
      .then(res => {
        console.log(res.data)
        this.load = false
        this.$router.push('/ticket')
      })
      
    }
  }
  
}
</script>
<style>
.display-2{
  font-weight: 600;
}

.center{
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
}

.form-label{
  font-weight: 900;
}
.display-4{
  font-weight: 400;
}

.button-top{
  margin-top: 2.2rem;
}

li { cursor: pointer; }

.info{
  color:crimson
}
.point{
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
}
.for-form{
  display: flex;
  flex-direction: column;
  align-items: center;
  
}


</style>