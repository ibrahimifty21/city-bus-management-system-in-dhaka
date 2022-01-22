<template>
    <div class="container">
        <div class="row">
            <h1 class="display-5 center mt-5 my-3">Here is our respected user thought 🗣</h1>
            <div v-for="r in review" :key="r.id" class="container my-1 ">
                <div class="card">
                <div class="card-body">
                    
                        <b>{{r.user_name}}</b>
                        <br>
                        
                        <small class="muted">{{r.created}}</small>

                        
                    
                    
                    <p class="card-text">
                        {{r.review}}
                    </p>
                    
                </div>
            </div>

            </div>
            <div class="row">
                <div class="d-flex flex-row justify-content-end">
                <div class="container">
                    <router-link to='/review_all'>See more</router-link>
                    
                </div>
                

            </div>
                

            </div>
            
            
            
        </div>
        <router-view></router-view>
    </div>
</template>
<script>
import axios from 'axios'
export default {
    name:'Review',
    data(){
        return{
            review:{}
        }
    },
    async created() {
        delete  axios.defaults.headers.common["Authorization"];
        await axios.get('api/review_limit/')
            .then(res => {
                this.review = res.data
                console.log(res.data)
                axios.defaults.headers.common['Authorization'] =  "Token "  +  localStorage.getItem('token')
            })
            .then(err => {
                console.log(err)
            })
        
    },
    
}
</script>
<style scoped>
.container{
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    
}
.card{
    width: 30rem ;
    
}

</style>