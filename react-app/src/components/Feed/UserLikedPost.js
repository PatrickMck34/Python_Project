import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import SinglePost from "../SinglePost";
import { getUserLikedPosts } from "../../store/posts";
import "./Feed.css"

export default function UserLikedPosts() {
    const dispatch = useDispatch();
    const userId = useSelector(state => state.session.user.id);

    const allPosts = useSelector(state => state.posts)
    const posts = allPosts.allPosts
    const session = useSelector(state => state.session)

    useEffect(() => {
        dispatch(getUserLikedPosts(userId))
    }, [dispatch, userId])

    return (
        <>
            <h2>Liked Posts</h2>
            <div id='dashboard'>
                <div id="user-liked-posts-feed">
                    {posts && Object.values(posts).map((post, idx) => (
                        <div className="post" key={idx}>
                            <div className="post-user-image-container">
                                <img className="post-user-image" src={post.user.profile_picture} alt='user profile'></img>
                            </div>
                            <div className="post-details">
                                <div className="post-user">
                                    <div className="user-username">{post.user.username}</div>
                                    <div className={`follow-user-button ${(post.user_id === session?.user?.id) && "hidden"}`}>Follow</div>
                                </div>
                                <h2 className="post-title">{post.post_title}</h2>
                                <img className={post.imageURL !== null ? "post-image" : "hidden"} src={post.imageURL} alt=''></img>
                                <div className={post.post_text ? "post-text" : "hidden"}>{post.post_text}</div>
                                <SinglePost info={[post, session]} />
                            </div>
                        </div>
                    )
                    )}
                </div>
                <div id='extras'>
                </div>
            </div>
        </>

    )
}
