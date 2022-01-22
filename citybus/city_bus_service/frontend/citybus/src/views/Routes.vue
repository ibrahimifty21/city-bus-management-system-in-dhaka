<template>
    <div class="container">
        <div class="my-3 text-center">
            <div class="display-6">
                Our bus stand
            </div>
            <div class="row">
                <div class="col-lg-4 col-md-6" v-for="route in route_name" :key="route.id">
                    <div class="card my-2">
                        <span class="mt-2">
                            <i class="fas fa-map-marker-alt"></i>
                        </span>
                        <div class="card-body">
                            {{route.name}}
                            <br>
                            📍 <b>{{route.longitude}} |
                            {{route.latitude}}</b>
                        </div>

                        
                    </div>
                </div>
                
            </div>
            
        </div>
        
       
    </div>
</template>
<script>
import axios from 'axios'
export default {
    name:'Route',
    data(){
        return{
            route_name:[]
        }
    },
    async created(){
        delete  axios.defaults.headers.common["Authorization"];
        await axios.get('api/route_name/')
        .then(res => {
            console.log(res)
            this.route_name = res.data.data
            axios.defaults.headers.common['Authorization'] =  "Token "  +  localStorage.getItem('token')

        })
    }
    
}
</script>
<style>
.display-5{
    font-weight: 500;
}   
.card{
    height: 13rem;
}
</style>